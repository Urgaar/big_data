from mrjob.job import MRJob

class TagCountPerUser(MRJob):

    def mapper(self, _, line):
        try:
            userID, movieID, tag, timestamp = line.split(',')
            yield userID, 1
        except ValueError:
            pass

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    TagCountPerUser.run()
